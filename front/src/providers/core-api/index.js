import LuminaMockProvider from "./LuminaMockProvider"
import LuminaProvider from "./LuminaProvider"

const isMockMode = process.env.VUE_APP_MODE === "frontend-only"

export default { lumina: isMockMode ? LuminaMockProvider : LuminaProvider }
