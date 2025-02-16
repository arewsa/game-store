<template>
  <button class="text-white m-2" @click="showSidebar = !showSidebar">
    <Icon icon="lucide:align-justify" height="40"></Icon>
  </button>
  <main
    class="absolute z-50 p-2 w-64 top-0 bg-white h-screen flex flex-col gap-2 items-start transform transition-transform duration-300 "
    :class="{ '-translate-x-0': showSidebar, '-translate-x-full': !showSidebar}"
  >
    <Icon icon="mynaui:accessibility" height="40" class="m-1 mb-6"> </Icon>
    <ItemOfSidebar title="Games" iconName="carbon:game-console" />
    <ItemOfSidebar title="Cart" iconName="mdi:cart-outline" />
    <ItemOfSidebar title="Add your card" iconName="icons8:plus"></ItemOfSidebar>
    <button @click="showSidebar = !showSidebar" v-on:click="$emit('onClick')">
      <Icon
        icon="humbleicons:times"
        height="30"
        class="absolute top-0 right-0 m-4"
      />
    </button>
  </main>
  <!-- <div class="blur-sm z-40 h-screen w-screen bg-opacity-50" v-if="showSidebar"></div> -->
</template>

<script setup lang="ts">
import { Icon } from "@iconify/vue/dist/iconify.js";
import ItemOfSidebar from "./ItemOfSidebar.vue";
import { ref } from "vue";
const showSidebar = ref(false);
</script>
