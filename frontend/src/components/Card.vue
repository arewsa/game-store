<template>
  <div class="bg-white rounded-md relative p-2 aspect-video">
    <img :src="'http://localhost:9000/product-image/' + game.img"  alt="" class="rounded-md shadow-2xl m-auto object-fill w-full h-full">
    <div class=" bottom-0 left-0 p-2">
      <p class="text-xl font-bold"> {{ game.name }} </p>
      <span class=""> {{ game.price }}$ </span>
    </div>
    <button v-if="!(gameStore.gamesIdInCart.includes(game.id))" class="absolute bottom-0 right-0 m-2 bg-blue-600 p-1 rounded-md hover:bg-blue-700 text-gray-100 font-semibold" @click="addToCart" > Add to Cart </button>
    <button v-if="(gameStore.gamesIdInCart.includes(game.id))" class="absolute bottom-0 right-0 m-2 bg-green-500 p-1 rounded-md hover:bg-green-600 text-gray-100 font-semibold" @click="removeFromCart" > Remove from Cart </button>
  </div>
</template>

<script setup lang="ts">
import { useGamesStore } from "../stores/gameStore";

const gameStore = useGamesStore();
const { game } = defineProps(["game"]);
function addToCart()
{
  gameStore.addGameToCart(game.id)
}

function removeFromCart()
{
  gameStore.removeGameFromCart(game.id)
}
</script>

<style scoped></style>
