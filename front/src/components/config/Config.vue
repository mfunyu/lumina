<template>
  <div class="flex gap-5">
    <div class="">
      <p class="text-indigo-600 font-bold text-2xl">rooms</p>

    </div>
    <div class="">
      <p class="text-indigo-600 font-bold text-2xl">entities</p>
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

export default {
  name: "Config",
  components: { Item },
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
