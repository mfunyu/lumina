<template>
  <button
    type="submit"
    :disabled="disabled || loading"
    class="
      inline-flex justify-center items-center py-2 px-4 border border-transparent shadow-sm font-medium rounded-md
      transition-colors duration-300
      focus:outline-none
      disabled:bg-gray-300 disabled:text-gray-400 disabled:cursor-not-allowed"
    :class="classes">
    {{ label }}
    <span
      v-if="emoji"
      class="ml-4">{{ emoji }}</span>
    <loading
      v-if="loading"
      :size="18"
      class="animate-spin ml-2" />
  </button>
</template>

<script>
export default {
  name: "Button",
  props: {
    label: {
      type: String,
      required: true
    },
    size: {
      type: String,
      default: "normal"
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    loading: {
      type: Boolean,
      default: false,
    },
    emoji: {
      type: String,
      required: false
    },
    secondary: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    classes() {
      const color = this.secondary ? "bg-stone-300 hover:bg-stone-200 focus:bg-stone-400"
        : " text-white bg-indigo-600 hover:bg-indigo-500 focus:bg-indigo-700"
      const SIZES_MAP = { large: "uppercase text-2xl py-3 px-7 font-bold tracking-wider" }
      return `${color} ${SIZES_MAP[this.size]}` || `${color}`
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
