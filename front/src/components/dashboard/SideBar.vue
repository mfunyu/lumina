<template>
  <div class="flex flex-col gap-5 m-3 items-center p-4 py-6 bg-stone-100 rounded-2xl">
    <div
      v-for="category in categories"
      :key="category"
      @click="onClickCategory(category)">
      <component
        :is="getIconCategory(category)"
        :size="30"
        :class="[category === currentCategory ? activeClass : inactiveClass]" />
    </div>
  </div>
</template>

<script>
export default {
  name: "SideBar",
  props: {
    setCategoryFilter: {
      type: Function,
      required: true
    }
  },
  data() {
    return { currentCategory: "" }
  },
  computed: {
    categories() {
      return ["sensor", "light", "switch", "multimedia", "air_conditioner"]
    },
    activeClass() {
      return "text-indigo-600 cursor-default transition-colors duration-200 ease-in-out"
    },
    inactiveClass() {
      return "text-stone-300 cursor-pointer hover:text-indigo-800 transition-colors duration-200 ease-in-out"
    }
  },
  methods: {
    onClickCategory(category) {
      if (this.currentCategory === category) {
        this.setCategoryFilter("")
        this.currentCategory = ""
        return
      }
      this.setCategoryFilter(category)
      this.currentCategory = category
    },
    getIconCategory(category) {
      if (category === "sensor") {
        return "sensor"
      } else if (category === "light") {
        return "lightbulb"
      } else if (category === "switch") {
        return "lightswitch"
      } else if (category === "multimedia") {
        return "multimedia"
      } else if (category === "air_conditioner") {
        return "airconditioner"
      }
      return null
    },
  }
}

</script>
