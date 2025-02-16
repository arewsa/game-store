<template>
  <div class="flex p-6">
    <div
      class="grid grid-cols-6 grid-rows-3 gap-5 grid-flow-row flex-auto grow-0 m-auto"
    >
      <Card
        :gameName="game.nameOfGame"
        :gameImg="game.img"
        :gamePrice="game.price"
        v-for="game in listOfGames"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import Card from "./Card.vue";

type Game = {
  price: number;
  img: string;
  nameOfGame: string;
}

let listOfGames: Game[] = [
{nameOfGame: "Elden Ring", img: "EldenRing.png", price: 123},
{nameOfGame: "Elden Ring", img: "EldenRing.png", price: 123}
]
</script>

<style scoped></style>
