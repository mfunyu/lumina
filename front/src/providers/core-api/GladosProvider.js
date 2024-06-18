import coreApiClient from "@/providers/core-api/CoreApi"

export default {
  getEntities() {
    return coreApiClient.sendRequest("get", "/entities", {})
  },
  getRooms() {
    return coreApiClient.sendRequest("get", "/rooms", {})
  }
}
