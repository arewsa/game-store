import { defineStore } from "pinia";
import { fetchWithCredentials } from "../services/auth";

export type Game = {
    price: number;
    img: string;
    name: string;
    id: number;
  }

export const useGamesStore = defineStore("games", {
  persist: true,
  state: () => ({
    games: [] as Game[],
    gamesIdInCart: [] as number[],
  }),
  getters: {
    getGames: (state) => {return state.games},
    gamesInCart: (state) =>
      state.games.filter((game) => state.gamesIdInCart.includes(game.id)),
  },
  actions: {
    async fetchGames() {
      const response = await fetchWithCredentials("http://localhost:8000/products?product_type=game", {
        method: "GET",
      });
      if (response != null)
      {
	const data = await response.json()
        this.games = data;
      }
      
    },
    addGameToCart(gameId: number) {
      this.gamesIdInCart.push(gameId);
    },
    removeGameFromCart(gameId: number){
      this.gamesIdInCart = this.gamesIdInCart.filter(game => game != gameId);
    },
    getTotal() {
      let total = 0;
      this.gamesInCart.forEach((game) => {
        total += game.price;
      });
      return total;
    }
  },
});
