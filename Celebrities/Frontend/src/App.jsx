import { BrowserRouter, Routes, Route } from "react-router-dom";
import CelebrityList from "./CelebrityList";
import CelebrityDetail from "./CelebrityDetail";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<CelebrityList />} />
        <Route path="/celebrity/:id" element={<CelebrityDetail />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
