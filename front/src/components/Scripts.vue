<template>
  <v-expansion-panels multiple>
    <v-expansion-panel>
      <v-expansion-panel-title>
        操作面板
      </v-expansion-panel-title>

      <v-expansion-panel-text >
        <v-row>
            <v-btn color="primary" block class="mb-3" @click="$GetRequest('api/v1/scripts/get_selected_assets')">打印所选资产</v-btn>
        </v-row>
        <v-row>
            <v-btn color="secondary" block class="mb-3">打开当前资产</v-btn>
        </v-row>
        <v-row>
            <v-btn color="success" block class="mb-3">测试1</v-btn>
        </v-row>
        <v-row>
            <v-btn color="warning" block class="mb-3">测试2</v-btn>
        </v-row>
        <v-row>
            <v-btn color="error" block>按钮1</v-btn>
        </v-row>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
  <v-file-upload
    browse-text="Local Filesystem"
    divider-text="or choose locally"
    icon="mdi-upload"
    title="Drag and Drop Here"
  ></v-file-upload>
</template>

<script setup>
</script>
