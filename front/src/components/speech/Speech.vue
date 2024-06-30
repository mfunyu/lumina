<template>
  <div
    @click="toggleSpeech"
    :class="[secondary ? secondaryClass : primaryClass]">
    <volumehigh
      v-if="!isSpeaking"
      :size="24"
      :class="[secondary ? 'text-stone-600' : 'text-white']"/>
    <pause
      v-else
      :size="24"
      :class="[secondary ? 'text-stone-600' : 'text-white']"/>
  </div>
</template>

<script>
import { useSpeechSynthesis } from "@vueuse/core"

export default {
  name: "Speech",
  props: {
    text: String,
    secondary: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    primaryClass() {
      return "fixed bottom-10 right-10 bg-indigo-500 text-white border-none rounded-full w-12 h-12 flex items-center justify-center shadow-md hover:bg-indigo-600 cursor-pointer transition-colors duration-300"
    },
    secondaryClass() {
      return ""
    }
  },
  data() {
    return { isSpeaking: false }
  },
  methods: {
    toggleSpeech() {
      const speech = useSpeechSynthesis(this.text)

      console.log("status", speech.status.value)
      if (this.isSpeaking) {
        window.speechSynthesis.pause()
        this.isSpeaking = false
      } else if (speech.status.value === "pause") {
        window.speechSynthesis.resume()
        this.isSpeaking = true
      } else {
        speech.speak()
        this.isSpeaking = true
      }
    }
  }
}
</script>
