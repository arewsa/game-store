<template>
  <div class="flex p-6">
    <div class="grid grid-cols-6 grid-rows-3 gap-5">
      <div class="col-span-5 grid-flow-row grow-0 m-auto">
        <div class="grid grid-cols-5 gap-4">
          <Card :game="game" v-for="game in gameStore.gamesInCart" />
        </div>
      </div>
      <div
        v-if="gameStore.gamesInCart.length > 0"
        class="col-start-6 row-span-2 bg-blue-100 p-4 rounded-lg self-start relative right-0"
      >
        <div class="flex flex-col">
          <h3 class="font-bold mb-2">Products</h3>
          <p class="mt-10">Total: {{ gameStore.getTotal() }}$</p>
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded right-0 static">
            Purchase
          </button>
        </div>
      </div>
    </div>
  </div>
  <div v-if="gameStore.gamesInCart.length == 0" class="text-2xl text-white text-center">
    Nothing in cart( Let's buy something
  </div>
</template>

<script setup lang="ts">
import Card from "./Card.vue";
import { useGamesStore } from "../stores/gameStore";

const gameStore = useGamesStore()

</script>

<style scoped></style>
