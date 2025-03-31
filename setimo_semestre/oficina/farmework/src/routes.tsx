import { createBrowserRouter } from "react-router";
import { Sobre } from "./components/sobre";
import { Home } from "./pages/home";
import { Layout } from "./_layout/layout";

export const router = createBrowserRouter([
    {
        path: '/',
        element: <Layout />,
        children: [
            { path: '/', element: <Home /> },
            { path: '/sobre', element: <Sobre /> },
            { path: '/servicos', element: <div>Serviços</div> },
            { path: '/contato', element: <div>Contato</div> },
        ]
    },
]);