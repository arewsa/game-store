<template>
    <div class="fixed top-5 right-5" v-if="open">
      <div
        id="toast-notification"
        class="w-full max-w-xs p-4 text-gray-900 bg-white rounded-lg shadow-sm dark:bg-gray-800 dark:text-gray-300"
        role="alert"
      >
        <div class="flex items-center mb-3">
          <span class="text-sm font-semibold text-gray-900 dark:text-white"
            >New notification</span
          >
          <button
            type="button"
            class="ms-auto -mx-1.5 -my-1.5 bg-white justify-center items-center shrink-0 text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700"
            data-dismiss-target="#toast-notification"
            aria-label="Close"
            @click="open = !open"
          >
            <span class="sr-only">Close</span>
            <svg
              class="w-3 h-3"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 14 14"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
              />
            </svg>
          </button>
        </div>
        <div
          class="absolute rounded-full -left-1 -top-1 bg-red-700 h-3 w-3 animate-ping"
        ></div>
        <div
          class="absolute rounded-full -left-1 -top-1 bg-red-700 h-3 w-3"
        ></div>
        <div class="flex items-center">
          <div class="ms-3 text-sm font-normal">
            <div class="text-lg font-semibold text-gray-900 dark:text-white">
              {{ message }}
            </div>
            <div class="text-sm font-normal text-right`">
              {{ description }}
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script setup lang="ts">

defineProps(["message", "description"])
const open = defineModel()
</script>