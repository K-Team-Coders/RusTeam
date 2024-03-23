import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/search_document",
    name: "SeacrhDocs",
    props(route) {
      return { text: route.query.text };
    },

    component: () => import("../views/SearchDocument.vue"),
  },
  {
    path: "/tender",
    name: "Tenders",

    component: () => import("../views/Tender.vue"),
  },
  {
    path: "/",
    name: "Mainpage",

    component: () => import("../views/MainPage.vue"),
  },
  {
    path: "/notfound",
    name: "NotFound",
    component: () => import("../components/PageNotFound.vue"),
    props: true,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
