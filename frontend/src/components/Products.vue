<template>
  <div class="flex p-6">
    <div
      class="grid grid-cols-6 grid-rows-3 gap-5 grid-flow-row flex-auto grow-0 m-auto"
    >
      <Card
        :game="game"
        v-for="game in gameStore.getGames"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import Card from "./Card.vue";
import { onMounted } from "vue";
import { useGamesStore } from "../stores/gameStore";

const gameStore = useGamesStore();

onMounted(async () => {
  gameStore.fetchGames();
});
</script>

<style scoped></style>
