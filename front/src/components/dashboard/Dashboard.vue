<template>
  <div class="flex flex-col gap-5">
    <div class="relative flex items-center">
      <ScrolleBar
        :rooms="rooms"
        :currentRoomId="currentRoomId"
        :getEntitiesByRoom="getEntitiesByRoom"/>
    </div>
    <div class="flex items-start">
      <SideBar :setCategoryFilter="setCategoryFilter"/>
      <div
        v-if="isLoading"
        class="text-gray-600">Loading...</div>
      <div
        v-else-if="isError"
        class="text-red-600">Error: failed to load data</div>
      <div v-else>
        <div class="flex flex-wrap items-stretch">
          <div
            v-for="entity in entities"
            :key="entity.id" >
            <Item
              v-if="!currentFilter || entity.type === currentFilter"
              @click="changeStatus(entity)"
              :item="entity" />
          </div>
        </div>
      </div>
    </div>
    <Speech :text="speechText()"/>
  </div>
</template>

<script>
import coreApi from "@/providers/core-api"
import Item from "@/components/cards/Item"
import ScrolleBar from "@/components/dashboard/ScrolleBar.vue"
import SideBar from "@/components/dashboard/SideBar.vue"
import Speech from "@/components/speech/Speech.vue"

export default {
  name: "Dashboard",
  components: {
    Item,
    ScrolleBar,
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
      currentRoomId: "",
      currentFilter: "",
      text: "Hello. Wellcome to Glados Dashboard! These are the current status. "
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
      if (this.currentRoomId === roomId) {
        this.getEntities()
        this.currentRoomId = ""
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
    setCategoryFilter(category) {
      this.currentFilter = category
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
      if (this.currentFilter) {
        text += `filtering ${this.currentFilter} entities. `
      }
      for (const entity of this.entities) {
        if (this.currentFilter && entity.type !== this.currentFilter)
          continue
        text += `${entity.name} is ${entity.status}. `
      }
      this.text = ""
      return text
    }
  }
}
</script>
