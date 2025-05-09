<template>
  <div class="w-48 hover:bg-gray-200 pl-2 rounded-md flex">
    <Icon :icon=iconName class="my-auto" height="30" :ssr="true"/>
    <button class="text-xl font-bold pl-4" @click="$router.push(route)">{{ title }}</button> 
  </div>
</template>

<script setup lang="ts">
import { Icon } from "@iconify/vue";
const { route } = defineProps(["title", "iconName", "route"]);
</script>
