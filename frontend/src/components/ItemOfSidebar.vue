<template>
  <div class="w-48 hover:bg-gray-200 pl-2 rounded-md flex">
    <Icon :icon=iconName class="my-auto" height="30" :ssr="true" />
    <h1 class="text-xl font-bold pl-4">{{ title }}</h1> 
  </div>
</template>

<script setup lang="ts">
import { Icon } from "@iconify/vue";
defineProps(["title", "iconName"]);
</script>
