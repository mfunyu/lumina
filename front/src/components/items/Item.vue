<template>
  <div class="item-container flex m-3 py-2 px-5 rounded-md bg-gray-200 shadow-sm">
    <div>
      <h2 class="mt-4 text-gray font-bold">{{ item.name }}</h2>
      <p class="mt-2 text-gray-600">{{ item.status }}</p>
      <p class="mt-2 text-gray-600">{{ item.description }}</p>
    </div>
    <lightbulboff
      v-if="item.type === 'light' && item.status === 'off'"
      class="my-auto"
      :size="60"
      :fillColor="'gray'" />
    <lightbulb
      v-else-if="item.type === 'light' && item.status === 'on'"
      class="my-auto"
      :size="60"
      :fillColor="'yellow'" />
    <lightswitch
      v-else-if="item.type === 'switch' && item.status === 'on'"
      class="my-auto"
      :size="60"
      :fillColor="'yellow'" />
    <lightswitchoff
      v-else-if="item.type === 'switch' && item.status === 'off'"
      class="my-auto"
      :size="60"
      :fillColor="'gray'" />
    <div
      v-else-if="item.value"
      class="my-auto flex"
      :style="{ 'min-width': '60px' }">
      <p class="m-auto text-3xl text-gray-600">{{ item.value }}</p>
      <span
        v-if="item.type === 'air_conditioner'"
        class="mt-2 m-1">
        &#8451;
      </span>
    </div>
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
  width: 25%;
  /* Set your desired width */
  min-width: 200px;
  justify-content: space-between;
}

.item-img {
  height: 100%;
}
</style>
