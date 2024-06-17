<template>
  <div class="item-container flex flex-col m-3 py-2 px-5 rounded-md bg-gray-200 shadow-sm">
    <!-- <img
      :src="item.image"
      :alt="item.name"
      class="w-32 h-32 object-cover rounded-full" /> -->
    <h2 class="mt-4 text-gray font-bold">{{ item.name }}</h2>
    <p class="mt-2 text-gray-600">{{ item.status }}</p>
    <p class="mt-2 text-gray-600">{{ item.description }}</p>
  </div>
</template>

<script>

export default {
  name: "Item",
  props: {
    item: {
      type: Object,
      required: true
    }
  }
}

</script>

<style scoped>
.item-container {
  width: 25%;  /* Set your desired width */
  min-width: 200px;
}
</style>