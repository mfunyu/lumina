<template>
  <div class="flex flex-col gap-5">
    <span class="text-indigo-600 font-bold text-2xl">Dashboard</span>
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
import Item from "@/components/items/Item"

export default {
  name: "Dashboard",
  components: { Item },
  created() {
    this.getEntities()
  },
  data() {
    return {
      entities: [],
      isLoading: false,
      isError: false
    }
  },
  methods: {
    getEntities() {
      this.isLoading = true

      coreApi.glados.getEntities()
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
    }
  }
}
</script>