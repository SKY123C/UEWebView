<!-- FolderBrowser.vue (Vuetify 3 · 仅文件夹浏览器) -->
<template>
  <v-container fluid class="fill-height">
    <v-row no-gutters class="h-100">
      <v-col cols="12" class="pa-2">
        <v-card class="h-100">
          <v-toolbar density="compact" title="Folders"></v-toolbar>
          <v-divider />

          <v-treeview
            :items="folders"
            item-title="name"
            item-value="id"
            open-on-click
            activatable
            @update:activated="onSelect"
          >
            <!-- 文件夹图标 -->
            <template #prepend="{ item, isOpen }">
              <v-icon size="18">
                {{ isOpen ? 'mdi-folder-open' : 'mdi-folder' }}
              </v-icon>
            </template>
          </v-treeview>

          <v-divider />
          <v-card-text>
            <div v-if="selected">
              <b>当前选择路径：</b>
              <div class="text-medium-emphasis">{{ selected.path }}</div>
            </div>
            <div v-else class="text-medium-emphasis">请选择一个文件夹</div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'

// 仅文件夹结构（无文件）
const folders = ref([
  {
    id: 1,
    name: 'assets',
    path: '/assets',
    children: [
      { id: 11, name: 'images', path: '/assets/images' },
      { id: 12, name: 'icons', path: '/assets/icons' },
    ],
  },
  {
    id: 2,
    name: 'src',
    path: '/src',
    children: [
      { id: 21, name: 'components', path: '/src/components' },
      { id: 22, name: 'views', path: '/src/views' },
    ],
  },
])

const selected = ref(null)

function onSelect(ids) {
  const id = ids?.[0]
  selected.value = findById(folders.value, id)
}

function findById(nodes, id) {
  for (const n of nodes) {
    if (n.id === id) return n
    if (n.children) {
      const f = findById(n.children, id)
      if (f) return f
    }
  }
  return null
}
</script>

<style scoped>
.h-100 { height: 100%; }
</style>