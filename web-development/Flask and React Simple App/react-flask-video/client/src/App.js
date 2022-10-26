import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
	const [data, setData] = useState([])
	const [isLoading, setisLoading] = useState(false)

	useEffect(() => {
		const fetchData = async () => {
			setisLoading(true)
			const response = await axios.get('/members')
			const members = response.data.members
			setData(members)
			setisLoading(false)
		}

		fetchData()
	}, [])

	return (
		<div className='App'>
			{isLoading ? (
				<h1>Loading</h1>
			) : (
				<div>
					{data.map((member, idx) => (
						<h1 key={idx}>{member}</h1>
					))}
				</div>
			)}
		</div>
	)
}

export default App
