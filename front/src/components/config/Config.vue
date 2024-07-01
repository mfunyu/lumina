<template>
  <div class="flex flex-col gap-5">
    <div class="flex items-center justify-between px-5">
      <div class="flex items-center gap-2">
        <p class="text-indigo-600 font-bold text-2xl">rooms</p>
        <Speech
          :text="roomSpeechText"
          :secondary="true"/>
      </div>
      <button
        @click="openNewRoomModal"
        class="text-indigo-600 font-bold text-3xl">+</button>
    </div>
    <div class="flex overflow-scroll">
      <Room
        @click="openRoomModal(room)"
        @delete="deleteRoom(room.id)"
        v-for="room in rooms"
        :deleteEnabled="true"
        :key="room.id"
        :room="room" />
    </div>
    <hr class="border-gray-300 my-4" />
    <div class="flex items-center justify-between px-5">
      <div class="flex items-center gap-2">
        <p class="text-indigo-600 font-bold text-2xl">entities</p>
        <Speech
          :text="itemSpeechText"
          :secondary="true"/>
      </div>
      <button
        @click="openNewItemModal"
        class="text-indigo-600 font-bold text-3xl">+</button>
    </div>
    <div class="flex items-start">
      <SideBar :setCategoryFilter="setCategoryFilter"/>
      <div class="flex flex-wrap items-stretch">
        <div
          v-for="entity in entities"
          :key="entity.id" >
          <Item
            v-if="!currentFilter || entity.type === currentFilter"
            @click="openItemModal(entity)"
            @delete="deleteEntity(entity.id)"
            :deleteEnabled="true"
            :item="entity" />
        </div>
      </div>
    </div>
    <Modal
      v-if="isModalOpen"
      :title="modalTitle"
      :initialData="modalData"
      :isItem="isItemModal"
      :errorMessage="modalErrorMessage"
      :rooms="rooms"
      @close="closeModal"
      @save="handleSave" />
    <Speech :text="speechText" />
  </div>
</template>

<script>
import coreApi from "@/providers/core-api"
import Item from "@/components/cards/Item"
import Modal from "@/components/modal/Modal.vue"
import Room from "@/components/cards/Room.vue"
import SideBar from "@/components/dashboard/SideBar.vue"
import Speech from "@/components/speech/Speech.vue"

export default {
  name: "Config",
  components: {
    Item,
    Room,
    Modal,
    SideBar,
    Speech
  },
  created() {
    this.loadData()
  },
  data() {
    return {
      entities: [],
      rooms: [],
      isLoading: false,
      isError: false,
      isModalOpen: false,
      modalTitle: "",
      modalData: null,
      modalErrorMessage: undefined,
      isItemModal: false,
      currentFilter: "",
    }
  },
  computed: {
    speechText() {
      let text = "Hello. Wellcome to Glados Configuration! You can modify rooms and entities here. "
      return text
    },
    roomSpeechText() {
      let text = "These are current rooms. "
      for (const room of this.rooms) {
        text += `${room.name} `
      }
      return text
    },
    itemSpeechText() {
      let text = "These are current entities. "
      if (this.currentFilter) {
        text += `Filtering by ${this.currentFilter}. `
      }
      for (const entity of this.entities) {
        if (this.currentFilter && entity.type !== this.currentFilter)
          continue
        text += `${entity.name} is ${entity.status}. `
      }
      return text
    }
  },
  methods: {
    loadData() {
      this.isLoading = true
      this.isError = false

      Promise.all([this.getEntities(), this.getRooms()])
        .finally(() => {
          this.isLoading = false
        })
    },
    getEntities() {
      return coreApi.glados.getEntities()
        .then((entities) => {
          this.entities = entities
        })
        .catch((error) => {
          console.error(error)
          this.isError = true
        })
    },
    getRooms() {
      return coreApi.glados.getRooms()
        .then((rooms) => {
          this.rooms = rooms
        })
        .catch((error) => {
          console.error(error)
          this.isError = true
        })
    },
    openRoomModal(room) {
      this.isModalOpen = true
      this.modalTitle = "Edit Room"
      this.modalData = room
      this.modalErrorMessage = undefined
      this.isItemModal = false
    },
    openItemModal(item) {
      this.isModalOpen = true
      this.modalTitle = "Edit Item"
      this.modalData = item
      this.modalErrorMessage = undefined
      this.isItemModal = true
    },
    openNewRoomModal() {
      this.isModalOpen = true
      this.modalTitle = "New Room"
      this.modalData = { name: "" }
      this.modalErrorMessage = undefined
      this.isItemModal = false
    },
    openNewItemModal() {
      this.isModalOpen = true
      this.modalTitle = "New Item"
      this.modalData = {
        name: "",
        status: "",
        type: "",
        value: "",
        roomId: "",
      }
      this.modalErrorMessage = undefined
      this.isItemModal = true
    },
    closeModal() {
      this.isModalOpen = false
      this.modalData = null
    },
    handleSave(data) {
      if (this.isItemModal) {
        if (this.modalData.id) {
          return coreApi.glados.changeEntityData(this.modalData.id, data)
            .then((updatedEntity) => {
              const index = this.entities.findIndex((entity) => entity.id === updatedEntity.id)
              if (index !== -1) {
                this.entities[index] = updatedEntity
              }
              this.closeModal()
            })
            .catch((error) => {
              this.modalErrorMessage = error.data.errors
            })
        } else {
          return coreApi.glados.createEntity(data)
            .then((newEntity) => {
              this.entities.push(newEntity)
              this.closeModal()
            })
            .catch((error) => {
              this.modalErrorMessage = error.data.errors
            })
        }
      } else {
        if (this.modalData.id) {
          return coreApi.glados.changeRoomData(this.modalData.id, data)
            .then((updatedRoom) => {
              const index = this.rooms.findIndex((room) => room.id === this.modalData.id)
              if (index !== -1) {
                this.rooms[index] = updatedRoom
              }
              this.closeModal()
            })
            .catch((error) => {
              this.modalErrorMessage = error.data.errors
            })
        } else {
          return coreApi.glados.createRoom(data)
            .then((newRoom) => {
              this.rooms.push(newRoom)
              this.closeModal()
            })
            .catch((error) => {
              this.modalErrorMessage = error.data.errors
            })
        }
      }
    },
    deleteEntity(id) {
      coreApi.glados.deleteEntity(id)
        .then(() => {
          this.entities = this.entities.filter((entity) => entity.id !== id)
        })
        .catch((error) => {
          console.error(error)
        })
    },
    deleteRoom(id) {
      coreApi.glados.deleteRoom(id)
        .then(() => {
          this.rooms = this.rooms.filter((room) => room.id !== id)
        })
        .catch((error) => {
          console.error(error)
        })
    },
    setCategoryFilter(category) {
      this.currentFilter = category
    }
  }
}
</script>
