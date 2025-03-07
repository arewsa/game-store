<template>
  <div class="bg-white rounded-md relative p-2">
    <img :src="'/images/' + gameImg"  alt="" class="rounded-md shadow-2xl m-auto ">
    <div class=" bottom-0 left-0 p-2">
      <p class="text-xl font-bold"> {{ gameName }} </p>
      <span class=""> {{ gamePrice }}$ </span>
    </div>
    <button v-if="!isInCart" class="absolute bottom-0 right-0 m-2 bg-blue-600 p-1 rounded-md hover:bg-blue-700 text-gray-100 font-semibold"> Add to Cart </button>
    <button v-if="isInCart" class="absolute bottom-0 right-0 m-2 bg-green-500 p-1 rounded-md hover:bg-green-600 text-gray-100 font-semibold"> Remove from Cart </button>
  </div>
</template>

<script setup lang="ts">
defineProps(["gameName", "gamePrice", "gameImg", "isInCart"]);

</script>

<style scoped></style>
