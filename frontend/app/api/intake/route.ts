import { NextResponse } from "next/server"

export async function POST(request: Request) {
  try {
    const formData = await request.json()

    const response = await fetch("http://localhost:8000/api/intake", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData)
    })

    if (!response.ok) {
      throw new Error(`Failed to submit to backend: ${response.statusText}`)
    }

    const result = await response.json()

    return NextResponse.json({
      success: true,
      message: "Form submitted successfully",
      backend: result,
    })
  } catch (error) {
    console.error("Error forwarding form data to backend:", error)
    return NextResponse.json(
      { success: false, message: "Failed to submit form to backend" },
      { status: 500 }
    )
  }
}