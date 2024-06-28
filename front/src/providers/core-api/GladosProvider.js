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
  },
  changeRoomData(roomId, data) {
    return coreApiClient.sendRequest("put", `/rooms/${roomId}`, data)
  },
  createEntity(data) {
    return coreApiClient.sendRequest("post", "/entities", data)
  },
  createRoom(data) {
    return coreApiClient.sendRequest("post", "/rooms", data)
  },
  deleteEntity(entityId) {
    return coreApiClient.sendRequest("delete", `/entities/${entityId}`, {})
  },
  deleteRoom(roomId) {
    return coreApiClient.sendRequest("delete", `/rooms/${roomId}`, {})
  },
}
