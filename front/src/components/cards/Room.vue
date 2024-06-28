<template>
  <div class="flex relative m-3 py-2 px-5 justify-center rounded-md bg-stone-100 shadow-sm">
    <button
      v-if="deleteEnabled"
      @click.stop="$emit('delete')"
      class="delete-button absolute top-2 right-2 text-stone-400 text-2xl hover:text-red-500">&times;</button>
    <h2 class="my-2 whitespace-nowrap">
      {{ room.name }}</h2>
  </div>
</template>

<script>

export default {
  name: "Room",
  props: {
    room: {
      type: Object,
      required: true
    },
    deleteEnabled: {
      type: Boolean,
      default: false
    }
  }
}

</script>
