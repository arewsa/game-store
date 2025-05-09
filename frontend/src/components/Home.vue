<template>
  <div>
    <div
      class="relative flex min-h-screen flex-col items-center justify-center px-6 lg:px-8"
    >
      <h1
        class="mt-8 text-6xl font-bold leading-tight text-white md:text-8xl w-screen text-center"
      >
        Buy game
        <span
          class="mt-2 block bg-gradient-to-r from-cyan-400 via-teal-400 to-emerald-400 bg-clip-text pb-4 text-transparent"
        >
          easier
        </span>
      </h1>
      <p
        class="mb-6 text-lg font-normal text-slate-300 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400 max-w-5xl text-center"
      >
      Wanted to buy the game?
        <span class="mt-2 block font-medium text-cyan-400">
          You're welcome!
        </span>
      </p>
      <RouterLink
        to="/main/games"
        class="inline-flex items-center justify-center text-base text-center bg-gradient-to-r from-cyan-500 to-teal-500 px-8 py-4 font-medium text-white transition-transform hover:scale-105 rounded-lg"
      >
        Lets start
        <svg
          class="w-3.5 h-3.5 ms-2 rtl:rotate-180"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 14 10"
        >
          <path
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M1 5h12m0 0L9 1m4 4L9 9"
          />
        </svg>
      </RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped></style>
