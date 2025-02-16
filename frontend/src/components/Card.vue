<template>
  <div class="bg-white rounded-md relative">
    <img src="../assets/images/EldenRing.png" alt="" class="rounded-md shadow-2xl m-2">
    <div class="bottom-0 left-0 p-2">
      <p class="text-xl font-bold"> {{ gameName }} </p>
      <span class=""> {{ gamePrice }}$ </span>
    </div>
    <button class="absolute bottom-0 right-0 m-2 bg-blue-600 p-1 rounded-md hover:bg-blue-700"> Add to Cart </button>
  </div>
</template>

<script setup lang="ts">
defineProps(["gameName", "gamePrice", "gameImg"]);

</script>

<style scoped></style>
