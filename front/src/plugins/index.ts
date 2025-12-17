import createVuetify from './vuetify'
import scripts from './scripts'
import type { App } from 'vue'

export function registerPlugins(app: App)
{
  app.config.globalProperties.$GetRequest = scripts.GetRequest
  app.use(createVuetify)
}