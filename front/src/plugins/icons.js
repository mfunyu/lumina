// https://materialdesignicons.com/
/* eslint-disable*/
import Loading from "vue-material-design-icons/Loading.vue"
import LightBulb from "vue-material-design-icons/Lightbulb.vue"
import LightbulbOutline from "vue-material-design-icons/LightbulbOutline.vue"
import LightSwitch from "vue-material-design-icons/LightSwitch.vue"
import LightSwitchOff from "vue-material-design-icons/LightSwitchOff.vue"

export default {
  install: (app, options) => {
    app.component("loading", Loading)
    app.component('lightbulb', LightBulb);
    app.component('lightbulboff', LightbulbOutline);
    app.component('lightswitch', LightSwitch);
    app.component('lightswitchoff', LightSwitchOff);
  }
}
