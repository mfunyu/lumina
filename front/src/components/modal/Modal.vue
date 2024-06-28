<template>
  <div
    v-if="isOpen"
    class="fixed inset-0 z-50 flex items-center justify-center bg-gray-800 bg-opacity-75">
    <div class="bg-white p-6 rounded-md shadow-md">
      <h2 class="text-xl font-bold mb-4">{{ title }}</h2>
      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Name</label>
          <input
            v-model="name"
            class="w-full border border-gray-300 p-2 rounded-md"
            type="text"
            required />
        </div>
        <div
          v-if="isItem"
          class="mb-4">
          <label class="block text-sm font-medium mb-1">Status</label>
          <input
            v-model="status"
            class="w-full border border-gray-300 p-2 rounded-md"
            type="text" />
        </div>
        <div
          v-if="isItem"
          class="mb-4">
          <label class="block text-sm font-medium mb-1">Type</label>
          <input
            v-model="type"
            class="w-full border border-gray-300 p-2 rounded-md"
            type="text" />
        </div>
        <div
          v-if="isItem"
          class="mb-4">
          <label class="block text-sm font-medium mb-1">Value</label>
          <input
            v-model="value"
            class="w-full border border-gray-300 p-2 rounded-md"
            type="text" />
        </div>
        <div class="flex justify-end gap-3">
          <Button
            label="Close"
            @click="close"
            :secondary=true />
          <Button
            label="Save"
            type="submit" />
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import Button from "@/components/buttons/Button.vue"

export default {
  name: "Modal",
  components: { Button },
  props: {
    isOpen: Boolean,
    title: String,
    initialData: Object,
    isItem: Boolean,
  },
  data() {
    return {
      name: this.initialData?.name || "",
      type: this.initialData?.type || "",
      status: this.initialData?.status || "",
      value: this.initialData?.value || ""
    }
  },
  methods: {
    close() {
      this.$emit("close")
    },
    handleSubmit() {
      if (this.isItem) {
        this.$emit("save", {
          name: this.name,
          type: this.type,
          status: this.status,
          value: this.value,
        })
      } else {
        this.$emit("save", { name: this.name, })
      }
    },
  },
  watch: {
    initialData(newData) {
      this.name = newData?.name || ""
      this.status = newData?.status || ""
      this.roomId = newData?.roomId || ""
      this.value = newData?.value || ""
      this.type = newData?.type || ""
    },
  },
}
</script>
