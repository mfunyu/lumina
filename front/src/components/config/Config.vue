<template>
  <div class="flex flex-col gap-5">
    <p class="px-5 text-indigo-600 font-bold text-2xl">rooms</p>
    <div class="flex overflow-scroll">
      <Room
        @click="openRoomModal(room)"
        v-for="room in rooms"
        :key="room.id"
        :room="room" />
    </div>
    <hr class="border-gray-300 my-4" />
    <p class="px-5 text-indigo-600 font-bold text-2xl">entities</p>
    <div class="flex flex-wrap">
      <Item
        @click="openItemModal(entity)"
        v-for="entity in entities"
        :key="entity.id"
        :item="entity" />
    </div>
    <Modal
      :isOpen="isModalOpen"
      :title="modalTitle"
      :initialData="modalData"
      :isItem="isItemModal"
      :errorMessage="modalErrorMessage"
      @close="closeModal"
      @save="handleSave" />
  </div>
</template>

<script>
import coreApi from "@/providers/core-api"
import Item from "@/components/cards/Item"
import Modal from "@/components/modal/Modal.vue"
import Room from "@/components/cards/Room.vue"

export default {
  name: "Config",
  components: {
    Item,
    Room,
    Modal
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
      modalErrorMessage: "",
      isItemModal: false,
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
      this.modalErrorMessage = ""
      this.isItemModal = false
      console.log(this.modalData.id)
    },
    openItemModal(item) {
      this.isModalOpen = true
      this.modalTitle = "Edit Item"
      this.modalData = item
      this.modalErrorMessage = ""
      this.isItemModal = true
    },
    closeModal() {
      this.isModalOpen = false
      this.modalData = null
    },
    handleSave(data) {
      if (this.isItemModal) {
        return coreApi.glados.changeEntityData(this.modalData.id, data)
          .then((updatedEntity) => {
            const index = this.entities.findIndex((entity) => entity.id === updatedEntity.id)
            if (index !== -1) {
              this.entities[index] = updatedEntity
            }
            this.closeModal()
          })
          .catch((error) => {
            console.error("myerror", error.data.errors)
            this.modalErrorMessage = error.data.errors
          })
      } else {
        return coreApi.glados.changeRoomData(this.modalData.id, data)
          .then((updatedRoom) => {
            const index = this.rooms.findIndex((room) => room.id === this.modalData.id)
            if (index !== -1) {
              this.rooms[index] = updatedRoom
            }
            this.closeModal()
          })
          .catch((error) => {
            console.error("myerror", error.data.errors)
            this.modalErrorMessage = error.data.errors
          })
      }
    },
  }
}
</script>
