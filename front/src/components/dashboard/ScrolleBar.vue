<template>
  <div
    class="flex gap-10 p-3 overflow-hidden px-10"
    ref="scrollContainer">
    <button
      @click="scrollLeft"
      class="absolute left-0 z-10 bg-white px-2 text-2xl text-grey-800">
      &lt;
    </button>
    <div
      v-for="room in rooms"
      :key="room.id">
      <span
        @click="onClickRoom(room.id)"
        class="text-xl whitespace-nowrap"
        :class="[ room.id === currentRoomId ? activeClass : inactiveClass ]">{{ room.name }}</span>
    </div>
    <button
      @click="scrollRight"
      class="absolute right-0 z-10 bg-white px-2 text-2xl text-grey-800">
      &gt;
    </button>
  </div>
</template>

<script>
export default {
  name: "ScrollBar",
  props: {
    rooms: {
      type: Array,
      required: true
    },
    currentRoomId: {
      type: String,
      required: true
    },
    getEntitiesByRoom: {
      type: Function,
      required: true
    }
  },
  data() {
    return { savedScrollPosition: 0 }
  },
  computed: {
    activeClass() {
      return "text-indigo-600 cursor-default font-bold border-b-2 border-indigo-600 transition-colors duration-200 ease-in-out"
    },
    inactiveClass() {
      return "text-gray-600 cursor-pointer hover:text-indigo-800 transition-colors duration-200 ease-in-out"
    }
  },
  methods: {
    onClickRoom(roomId) {
      this.saveScrollPosition()
      this.getEntitiesByRoom(roomId)
      this.restoreScrollPosition()
    },
    saveScrollPosition() {
      this.savedScrollPosition = this.$refs.scrollContainer.scrollLeft
    },
    restoreScrollPosition() {
      this.$nextTick(() => {
        this.$refs.scrollContainer.scrollLeft = this.savedScrollPosition
      })
    },
    scrollLeft() {
      this.$refs.scrollContainer.scrollBy({
        left: -150,
        behavior: "smooth"
      })
    },
    scrollRight() {
      this.$refs.scrollContainer.scrollBy({
        left: 150,
        behavior: "smooth"
      })
    },
  }
}
</script>

