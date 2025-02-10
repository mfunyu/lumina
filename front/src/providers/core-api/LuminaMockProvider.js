import mockDataFile from "@/data/data.json"

// Create a deep copy of the data to avoid modifying the original
const mockData = JSON.parse(JSON.stringify(mockDataFile))

const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms))

export default {
  async getEntities() {
    await delay(100)
    return mockData.entities
  },

  async getEntitiesByRoom(roomId) {
    await delay(100)
    return mockData.entities.filter((entity) => entity.room_id === roomId)
  },

  async getRooms() {
    await delay(100)
    return mockData.rooms
  },

  async changeEntityData(entityId, data) {
    await delay(100)
    const index = mockData.entities.findIndex((entity) => entity.id === entityId)
    if (index !== -1) {
      mockData.entities[index] = {
        ...mockData.entities[index],
        ...data
      }
      return mockData.entities[index]
    }
    throw new Error("Entity not found")
  },

  async changeRoomData(roomId, data) {
    await delay(100)
    const index = mockData.rooms.findIndex((room) => room.id === roomId)
    if (index !== -1) {
      mockData.rooms[index] = {
        ...mockData.rooms[index],
        ...data
      }
      return mockData.rooms[index]
    }
    throw new Error("Room not found")
  },

  async createEntity(data) {
    await delay(100)
    const newEntity = {
      id: String(mockData.entities.length + 1),
      ...data
    }
    mockData.entities.push(newEntity)
    return newEntity
  },

  async createRoom(data) {
    await delay(100)
    const newRoom = {
      id: String(mockData.rooms.length + 1),
      ...data
    }
    mockData.rooms.push(newRoom)
    return newRoom
  },

  async deleteEntity(entityId) {
    await delay(100)
    mockData.entities = mockData.entities.filter((entity) => entity.id !== entityId)
  },

  async deleteRoom(roomId) {
    await delay(100)
    mockData.rooms = mockData.rooms.filter((room) => room.id !== roomId)
  }
}
