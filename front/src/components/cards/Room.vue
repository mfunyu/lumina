<template>
  <div class="flex m-3 py-2 px-5 justify-center rounded-md bg-stone-100 shadow-sm">
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
    }
  }
}

</script>
