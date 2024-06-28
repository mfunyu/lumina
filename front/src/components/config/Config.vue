<template>
  <div class="flex flex-col gap-5">
    <p class="px-5 text-indigo-600 font-bold text-2xl">rooms</p>
    <div class="flex overflow-scroll">
      <Room
        v-for="room in rooms"
        :key="room.id"
        :room="room" />
    </div>
    <hr class="border-gray-300 my-4" />
    <p class="px-5 text-indigo-600 font-bold text-2xl">entities</p>
    <div class="flex flex-wrap">
      <Item
        v-for="entity in entities"
        :key="entity.id"
        :item="entity" />
    </div>
  </div>
</template>

<script>
import coreApi from "@/providers/core-api"
import Item from "@/components/cards/Item"
import Room from "../cards/Room.vue"

export default {
  name: "Config",
  components: {
    Item,
    Room
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
