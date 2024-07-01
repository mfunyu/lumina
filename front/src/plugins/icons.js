// https://materialdesignicons.com/
/* eslint-disable*/
import Loading from "vue-material-design-icons/Loading.vue"
import LightBulb from "vue-material-design-icons/Lightbulb.vue"
import LightbulbOutline from "vue-material-design-icons/LightbulbOutline.vue"
import LightSwitch from "vue-material-design-icons/LightSwitch.vue"
import LightSwitchOff from "vue-material-design-icons/LightSwitchOff.vue"
import Multimedia from "vue-material-design-icons/Multimedia.vue"
import Pause from "vue-material-design-icons/Pause.vue"
import VolumeHigh from "vue-material-design-icons/VolumeHigh.vue"
import Wifi from "vue-material-design-icons/Wifi.vue"
import AirConditioner from "vue-material-design-icons/AirConditioner.vue"

export default {
  install: (app, options) => {
    app.component("loading", Loading)
    app.component('lightbulb', LightBulb);
    app.component('lightbulboff', LightbulbOutline);
    app.component('lightswitch', LightSwitch);
    app.component('lightswitchoff', LightSwitchOff);
    app.component('volumehigh', VolumeHigh);
    app.component('pause', Pause);
    app.component('multimedia', Multimedia);
    app.component('sensor', Wifi);
    app.component('airconditioner', AirConditioner);
  }
}
