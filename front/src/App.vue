<template>
  <v-app>
      <SideNavigation />
      <v-main scrollable>
        
        <router-view v-slot="{ Component }">
          <keep-alive>
            <component :is="Component" />
          </keep-alive>
        </router-view>
      </v-main>
  </v-app>
</template>


