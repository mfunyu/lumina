<template>
  <div
    @click="playTextToSpeech"
    class="fixed bottom-10 right-10 bg-indigo-500 text-white border-none rounded-full w-12 h-12 flex items-center justify-center shadow-md hover:bg-indigo-600 cursor-pointer transition-colors duration-300">
    <volumehigh
      :size="24"
      class="text-white" />
  </div>
</template>

<script>
import { useSpeechSynthesis } from "@vueuse/core"

export default {
  name: "Speech",
  props: { text: String, },
  methods: {
    playTextToSpeech() {
      const speech = useSpeechSynthesis(this.text)
      if (speech.status.value === "pause") {
        console.log("resume")
        window.speechSynthesis.resume()
      }
      else {
        speech.speak()
      }
    }
  }
}
</script>
