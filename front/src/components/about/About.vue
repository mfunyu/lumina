<template>
  <div
    class="flex flex-col gap-5"
    ref="content">
    <div class="flex items-center gap-2">

      <span class="text-indigo-600 font-bold text-2xl">About</span>
      <Speech
        :text="speechText"
        :secondary="true"/>
    </div>
    <div class="flex flex-col gap-2 text-lg">
      <p>
        Lumina is an advanced system designed to connect homes worldwide, making them autonomous and highly efficient.
      </p>
      <p>
        It enhances convenience by automating tasks, controlling home environments remotely, and providing custom routines for users.
      </p>
      <p>
        Lumina optimizes energy usage, promotes the use of renewable energy, and encourages environmental responsibility. It also focuses on safety and accessibility, offering assistance to individuals with disabilities or the elderly and monitoring the health and safety of all residents.
      </p>
      <p>
        This innovative solution aims to transform how we interact with and manage our homes, creating a smarter, greener, and more inclusive living environment.
        <ul class="list-disc pl-5 inline-block">
          <li>
            By the Integration of AI and Machine Learning, Lumina adapts to user behavior over time, learning preferences and suggesting optimal settings for lighting, temperature, and energy usage, further enhancing the personalized smart home experience.          </li>
          <li>
            By the Use of Advanced IoT Technology, Lumina connects and synchronizes a wide range of devices, creating a seamless network that ensures all systems within the home work in harmony.          </li>
          <li>
            By the Implementation of Real-Time Monitoring, Lumina provides instant updates on energy consumption, device status, and potential safety concerns, allowing users to take immediate action when needed.          </li>
          <li>
            By the Emphasis on Scalability and Customization, Lumina supports the integration of new devices and technologies, making it future-ready and adaptable to diverse household needs and preferences.          </li>
        </ul>
      </p>
    </div>
  </div>
  <Speech :text="speechText" />
</template>

<script>
import Speech from "@/components/speech/Speech"

export default {
  name: "About",
  components: { Speech },
  data() {
    return { speechText: "This is About page. ", }
  },
  mounted() {
    this.extractTextContent()
  },
  methods: {
    extractTextContent() {
      const content = this.$refs.content
      console.log(content)
      this.speechText += content?.innerText || content?.textContent
    },
  },
}
</script>
