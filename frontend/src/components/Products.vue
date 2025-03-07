<template>
  <div class="flex p-6">
    <div
      class="grid grid-cols-6 grid-rows-3 gap-5 grid-flow-row flex-auto grow-0 m-auto"
    >
      <Card
        :gameName="game.game_name"
        :gameImg="game.game_img"
        :gamePrice="game.game_price"
        v-for="game in listOfGames"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import Card from "./Card.vue";
import { onMounted, ref } from 'vue'

type Game = {
  game_price: number;
  game_img: string;
  game_name: string;
  game_id: number;
}
let listOfGames = ref<Game[]>([])

onMounted(async () => {
  const response = await fetch("http://localhost:8000/games");  
  const data: Game[] = await response.json()
  listOfGames.value = data
})
</script>

<style scoped></style>
