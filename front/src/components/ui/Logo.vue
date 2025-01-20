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
import Logo from "@/assets/images/logo/logo_default.svg"
import LogoActive from "@/assets/images/logo/logo_default_active.svg"

export default {
  name: "Logo",
  data() {
    return {
      Logo,
      LogoActive,
      isHover: false
    }
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
