<template>
  <div class="item-container flex-grow relative flex m-3 py-2 px-5 rounded-md bg-stone-100 shadow-sm">
    <div>
      <button
        v-if="deleteEnabled"
        @click.stop="$emit('delete')"
        class="delete-button absolute top-2 right-2 text-stone-400 text-2xl hover:text-red-500">&times;</button>
      <h2
        class="mt-4 font-bold"
        :class="fontColor">
        {{ item.name }}</h2>
      <p
        class="mt-2"
        :class="fontColor">
        {{ item.status }}</p>
      <p
        class="mt-2"
        :class="fontColor">
        {{ item.description }}</p>
    </div>
    <component
      :is="iconComponent"
      v-if="iconComponent"
      class="my-auto"
      :size="60"
      :class="iconColor" />
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
    },
    deleteEnabled: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    fontColor() {
      return this.item.status === "unavailable" ? "text-gray-400" : "text-gray-600"
    },
    iconComponent() {
      if (this.item.type === "light") {
        return this.item.status === "on" ? "lightbulb" : "lightbulboff"
      } else if (this.item.type === "switch") {
        return this.item.status === "on" ? "lightswitch" : "lightswitchoff"
      }
      return null
    },
    iconColor() {
      if (this.item.status === "on") {
        return "text-yellow-400"
      } else if (this.item.status === "off") {
        return "text-gray-500"
      }
      return "text-gray-300"
    },
    valueColor() {
      if (this.item.status !== "on")
        return "text-gray-500"
      if (this.item.type === "air_conditioner") {
        return this.item.value >= 28 ? "text-green-400" : "text-blue-400"
      }
      return "text-yellow-400"
    }
  }
}

</script>

<style scoped>
.item-container {
  width: 20%;
  min-width: 250px;
  justify-content: space-between;
}

.item-img {
  height: 100%;
}
</style>
