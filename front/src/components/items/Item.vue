<template>
  <div class="item-container flex m-3 py-2 px-5 rounded-md bg-gray-200 shadow-sm">
    <div>
      <h2 class="mt-4 text-gray font-bold">{{ item.name }}</h2>
      <p class="mt-2 text-gray-600">{{ item.status }}</p>
      <p class="mt-2 text-gray-600">{{ item.description }}</p>
    </div>
    <component
      :is="iconComponent"
      v-if="iconComponent"
      class="my-auto"
      :size="60"
      :fillColor="iconColor" />
    <div
      v-else-if="item.value"
      class="my-auto flex"
      :style="{ 'min-width': '60px' }">
      <p
        class="m-auto text-3xl"
        :class="valueColor">{{ item.value }}</p>
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
  },
  computed: {
    iconComponent() {
      if (this.item.type === "light") {
        return this.item.status === "off" ? "lightbulboff" : "lightbulb"
      } else if (this.item.type === "switch") {
        return this.item.status === "off" ? "lightswitchoff" : "lightswitch"
      }
      return null
    },
    iconColor() {
      return this.item.status === "off" ? "gray" : "yellow"
    },
    valueColor() {
      if (this.item.status !== "on")
        return "text-gray-500"
      if (this.item.type === "air_conditioner") {
        return this.item.value >= 28 ? "text-green-400" : "text-blue-400"
      }
      return "text-yellow-500"
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
