<template>
  <div class="flex flex-col gap-5">
    <div
      v-if="isLoading"
      class="text-gray-600">Loading...</div>
    <div
      v-else-if="isError"
      class="text-red-600">Error loading data</div>
    <div v-else>
      <div class="flex gap-10 p-3">
        <div
          v-for="room in rooms"
          :key="room.id">
          <span class="text-gray-600 font-bold text-xl">{{ room.name }}</span>
        </div>
      </div>
      <div class="flex flex-wrap">
        <Item
          v-for="entity in entities"
          :key="entity.id"
          :item="entity" />
      </div>
    </div>
  </div>
</template>

<script>
import coreApi from "@/providers/core-api"
import Item from "@/components/items/Item"

export default {
  name: "Dashboard",
  components: { Item },
  created() {
    this.loadData()
  },
  data() {
    return {
      entities: [],
      rooms: [],
      isLoading: false,
      isError: false
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
    }
  }
}
</script>