<template>
  <div class="flex flex-col gap-5">
    <div class="relative flex items-center">
      <div
        class="flex gap-10 p-3 overflow-hidden px-10"
        ref="scrollContainer">
        <button
          @click="scrollLeft"
          class="absolute left-0 z-10 bg-white px-2 text-2xl text-grey-800">
          &lt;
        </button>
        <div
          v-for="room in rooms"
          :key="room.id">
          <span
            @click="getEntitiesByRoom(room.id)"
            class="text-xl whitespace-nowrap"
            :class="[ room.id === currentRoomId ? activeClass : inactiveClass ]">{{ room.name }}</span>
        </div>
        <button
          @click="scrollRight"
          class="absolute right-0 z-10 bg-white px-2 text-2xl text-grey-800">
          &gt;
        </button>
      </div>
    </div>
    <div
      v-if="isLoading"
      class="text-gray-600">Loading...</div>
    <div
      v-else-if="isError"
      class="text-red-600">Error: failed to load data</div>
    <div v-else>
      <div class="flex flex-wrap">
        <Item
          @click="changeStatus(entity)"
          v-for="entity in entities"
          :key="entity.id"
          :item="entity" />
      </div>
    </div>
    <Speech :text="speechText()"/>
  </div>
</template>

<script>
import coreApi from "@/providers/core-api"
import Item from "@/components/cards/Item"
import Speech from "@/components/speech/Speech.vue"

export default {
  name: "Dashboard",
  components: {
    Item,
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
      currentRoomId: null,
      savedScrollPosition: 0,
      text: "Hello. Wellcome to Glados Dashboard! These are the current status. "
    }
  },
  computed: {
    activeClass() {
      return "text-indigo-600 cursor-default font-bold border-b-2 border-indigo-600 transition-colors duration-200 ease-in-out"
    },
    inactiveClass() {
      return "text-gray-600 cursor-pointer hover:text-indigo-800 transition-colors duration-200 ease-in-out"
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
    getEntitiesByRoom(roomId) {
      this.saveScrollPosition()
      if (this.currentRoomId === roomId) {
        this.getEntities()
        this.currentRoomId = null
        return
      }

      this.currentRoomId = roomId
      this.isLoading = true

      coreApi.glados.getEntitiesByRoom(roomId)
        .then((entities) => {
          this.entities = entities
        })
        .catch((error) => {
          console.error(error)
          this.isError = true
        })
        .finally(() => {
          this.isLoading = false
          this.restoreScrollPosition()
        })
    },
    changeStatus(entity) {
      if (entity.status == "unavailable")
        return
      const newStatus = entity.status === "on" ? "off" : "on"
      coreApi.glados.changeEntityData(entity.id, { status: newStatus })
        .then((updatedEntity) => {
          const index = this.entities.findIndex(e => e.id === entity.id)
          if (index !== -1) {
            this.entities[index] = updatedEntity
          }
        })
        .catch((error) => {
          console.error(error)
          this.isError = true
        })
    },
    saveScrollPosition() {
      this.savedScrollPosition = this.$refs.scrollContainer.scrollLeft
    },
    restoreScrollPosition() {
      this.$nextTick(() => {
        this.$refs.scrollContainer.scrollLeft = this.savedScrollPosition
      })
    },
    scrollLeft() {
      this.$refs.scrollContainer.scrollBy({
        left: -150,
        behavior: "smooth"
      })
    },
    scrollRight() {
      this.$refs.scrollContainer.scrollBy({
        left: 150,
        behavior: "smooth"
      })
    },
    speechText() {
      let text = this.text

      if (this.currentRoomId) {
        const roomName = this.rooms.find(room => room.id === this.currentRoomId)?.name
        text += `In ${roomName}, `
      }
      if (this.entities.length === 0) {
        text += "there is no entities registered. "
      }
      for (const entity of this.entities) {
        text += `${entity.name} is ${entity.status}. `
      }
      this.text = ""
      return text
    }
  }
}
</script>
