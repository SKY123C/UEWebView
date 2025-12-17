<template>

      <v-navigation-drawer
        expand-on-hover
        permanent
        rail
      >
        <v-list>
          <v-list-item
            prepend-avatar="https://randomuser.me/api/portraits/women/85.jpg"
            subtitle="sandra_a88@gmailcom"
            title="Sandra Adams"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-folder" title="动画" value="animation" to="/animation"></v-list-item>
          <v-list-item prepend-icon="mdi-folder" title="材质" value="material" to="/material"></v-list-item>
          <v-list-item prepend-icon="mdi-folder" title="灯光" value="lighting" to="/lighting"></v-list-item>
          <v-list-item prepend-icon="mdi-folder" title="通用" value="utl" to="/utl"></v-list-item>
          <v-list-item prepend-icon="mdi-folder" title="检查" value="check" to="/check"></v-list-item>
          <v-list-item prepend-icon="mdi-star" title="Sequence" value="starred" to="/sequence"></v-list-item>
          <v-list-item prepend-icon="mdi-star" title="Scripts" value="Scripts" to="/scripts"></v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main style="height: 250px"></v-main>

</template>
