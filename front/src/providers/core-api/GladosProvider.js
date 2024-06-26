import coreApiClient from "@/providers/core-api/CoreApi"

export default {
  getEntities() {
    return coreApiClient.sendRequest("get", "/entities", {})
  },
  getEntitiesByRoom(roomId) {
    return coreApiClient.sendRequest("get", `/entities?room_id=${roomId}`, {})
  },
  getRooms() {
    return coreApiClient.sendRequest("get", "/rooms", {})
  },
  changeEntityData(entityId, data) {
    return coreApiClient.sendRequest("put", `/entities/${entityId}`, data)
  }
}
