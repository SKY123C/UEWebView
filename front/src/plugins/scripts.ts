import axios, { type ResponseType } from 'axios'

async function GetRequest(endpoint: string, resType: ResponseType = 'json')
{
  try {
    // 使用相对路径，通过 Vite 代理转发到后端
    const response = await axios.get(`/${endpoint}`, { responseType: resType})
    console.log('API Response:', response.data)
    return response.data
  } catch (error) {
    console.error('API Request failed:', error)
    throw error
  }
}

export default {
  GetRequest
}