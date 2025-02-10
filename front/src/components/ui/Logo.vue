<template>
  <div
    class="flex w-32 items-center"
    @mouseover="isHover = true"
    @mouseleave="isHover = false">
    <component
      :is="iconComponent"
      :size="45"
      :class="iconColor" />

    <div class="text-2xl text-gray-600 cursor-default font-bold">
      LUMINA
    </div>
  </div>
</template>

<script>

export default {
  name: "Logo",
  data() {
    return { isHover: false }
  },
  computed: {
    iconComponent() {
      return this.isHover ? "lightbulb" : "lightbulboff"
    },
    iconColor() {
      return this.isHover ? "text-yellow-400" : "text-gray-400"
    }
  }
}
</script>
