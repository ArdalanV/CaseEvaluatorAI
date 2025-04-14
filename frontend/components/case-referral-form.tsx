"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Checkbox } from "@/components/ui/checkbox"
import { Calendar } from "@/components/ui/calendar"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
import { format } from "date-fns"
import { CalendarIcon } from "lucide-react"
import { cn } from "@/lib/utils"
import { Label } from "@/components/ui/label"
import { Card, CardContent } from "@/components/ui/card"
import { useToast } from "@/hooks/use-toast"

export default function CaseReferralForm() {
  const { toast } = useToast()
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [date, setDate] = useState<Date | undefined>(undefined)

  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    phone: "",
    accident_type: "",
    num_involved_people: 1,
    is_injured: false,
    injury_types: "",
    sought_medical_care: false,
    filed_police_report: false,
    is_insured: false,
    insurance_coverage: "",
    has_witnesses: false,
    incident_date: "",
    has_affordability_concerns: false,
    city: "",
    state: "",
    incident_description: "",
    medical_costs: "",
  })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setFormData((prev) => ({ ...prev, [name]: value }))
  }

  const handleNumberChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target
    setFormData((prev) => ({ ...prev, [name]: Number.parseInt(value) || 0 }))
  }

  const handleCheckboxChange = (name: string, checked: boolean) => {
    setFormData((prev) => ({ ...prev, [name]: checked }))
  }

  const handleDateChange = (date: Date | undefined) => {
    setDate(date)
    if (date) {
      setFormData((prev) => ({
        ...prev,
        incident_date: format(date, "yyyy-MM-dd"),
      }))
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    if (!formData.first_name || !formData.last_name || !formData.email || !formData.phone) {
      toast({
        title: "Missing Information",
        description: "Please fill out all required fields.",
        variant: "destructive",
      })
      return
    }

    setIsSubmitting(true)

    try {
      const response = await fetch("/intake", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      })

      if (response.ok) {
        toast({
          title: "Form Submitted",
          description: "Your case has been successfully submitted for evaluation.",
        })

        // Reset form
        setFormData({
          first_name: "",
          last_name: "",
          email: "",
          phone: "",
          accident_type: "",
          num_involved_people: 1,
          is_injured: false,
          injury_types: "",
          sought_medical_care: false,
          filed_police_report: false,
          is_insured: false,
          insurance_coverage: "",
          has_witnesses: false,
          incident_date: "",
          has_affordability_concerns: false,
          city: "",
          state: "",
          incident_description: "",
          medical_costs: "",
        })
        setDate(undefined)
      } else {
        const errorData = await response.json()
        toast({
          title: "Submission Failed",
          description: errorData.detail || "There was an error submitting your form.",
          variant: "destructive",
        })
      }
    } catch (error) {
      toast({
        title: "Submission Error",
        description: "There was a problem connecting to the server.",
        variant: "destructive",
      })
      console.error("Error:", error)
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <Card className="shadow-lg">
      <CardContent className="p-6">
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <Label htmlFor="first_name">
                First Name <span className="text-red-500">*</span>
              </Label>
              <Input
                id="first_name"
                name="first_name"
                value={formData.first_name}
                onChange={handleChange}
                required
                minLength={2}
                maxLength={20}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="last_name">
                Last Name <span className="text-red-500">*</span>
              </Label>
              <Input
                id="last_name"
                name="last_name"
                value={formData.last_name}
                onChange={handleChange}
                required
                minLength={2}
                maxLength={20}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="email">
                Email <span className="text-red-500">*</span>
              </Label>
              <Input
                id="email"
                name="email"
                type="email"
                value={formData.email}
                onChange={handleChange}
                required
                minLength={3}
                maxLength={50}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="phone">
                Phone Number <span className="text-red-500">*</span>
              </Label>
              <Input
                id="phone"
                name="phone"
                type="tel"
                value={formData.phone}
                onChange={handleChange}
                required
                minLength={10}
                maxLength={10}
                placeholder="1234567890"
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="accident_type">
                Accident Type <span className="text-red-500">*</span>
              </Label>
              <Input
                id="accident_type"
                name="accident_type"
                value={formData.accident_type}
                onChange={handleChange}
                required
                minLength={3}
                maxLength={100}
                placeholder="Car accident, slip and fall, etc."
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="num_involved_people">
                Number of People Involved <span className="text-red-500">*</span>
              </Label>
              <Input
                id="num_involved_people"
                name="num_involved_people"
                type="number"
                min={1}
                value={formData.num_involved_people}
                onChange={handleNumberChange}
                required
              />
            </div>

            <div className="space-y-2 md:col-span-2">
              <div className="flex items-center space-x-2">
                <Checkbox
                  id="is_injured"
                  checked={formData.is_injured}
                  onCheckedChange={(checked) => handleCheckboxChange("is_injured", checked as boolean)}
                />
                <Label htmlFor="is_injured">Were you injured?</Label>
              </div>
            </div>

            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="injury_types">
                Injury Types <span className="text-red-500">*</span>
              </Label>
              <Textarea
                id="injury_types"
                name="injury_types"
                value={formData.injury_types}
                onChange={handleChange}
                required
                minLength={3}
                maxLength={512}
                placeholder="Describe your injuries"
                className="min-h-[80px]"
              />
            </div>

            <div className="space-y-2 md:col-span-2">
              <div className="flex items-center space-x-2">
                <Checkbox
                  id="sought_medical_care"
                  checked={formData.sought_medical_care}
                  onCheckedChange={(checked) => handleCheckboxChange("sought_medical_care", checked as boolean)}
                />
                <Label htmlFor="sought_medical_care">Did you seek medical care?</Label>
              </div>
            </div>

            <div className="space-y-2 md:col-span-2">
              <div className="flex items-center space-x-2">
                <Checkbox
                  id="filed_police_report"
                  checked={formData.filed_police_report}
                  onCheckedChange={(checked) => handleCheckboxChange("filed_police_report", checked as boolean)}
                />
                <Label htmlFor="filed_police_report">Did you file a police report?</Label>
              </div>
            </div>

            <div className="space-y-2 md:col-span-2">
              <div className="flex items-center space-x-2">
                <Checkbox
                  id="is_insured"
                  checked={formData.is_insured}
                  onCheckedChange={(checked) => handleCheckboxChange("is_insured", checked as boolean)}
                />
                <Label htmlFor="is_insured">Do you have insurance?</Label>
              </div>
            </div>

            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="insurance_coverage">
                Insurance Coverage <span className="text-red-500">*</span>
              </Label>
              <Input
                id="insurance_coverage"
                name="insurance_coverage"
                value={formData.insurance_coverage}
                onChange={handleChange}
                required
                minLength={3}
                maxLength={256}
                placeholder="Describe your insurance coverage"
              />
            </div>

            <div className="space-y-2 md:col-span-2">
              <div className="flex items-center space-x-2">
                <Checkbox
                  id="has_witnesses"
                  checked={formData.has_witnesses}
                  onCheckedChange={(checked) => handleCheckboxChange("has_witnesses", checked as boolean)}
                />
                <Label htmlFor="has_witnesses">Were there any witnesses?</Label>
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="incident_date">
                Incident Date <span className="text-red-500">*</span>
              </Label>
              <Popover>
                <PopoverTrigger asChild>
                  <Button
                    variant="outline"
                    className={cn("w-full justify-start text-left font-normal", !date && "text-muted-foreground")}
                  >
                    <CalendarIcon className="mr-2 h-4 w-4" />
                    {date ? format(date, "PPP") : <span>Select a date</span>}
                  </Button>
                </PopoverTrigger>
                <PopoverContent className="w-auto p-0">
                  <Calendar mode="single" selected={date} onSelect={handleDateChange} initialFocus />
                </PopoverContent>
              </Popover>
            </div>

            <div className="space-y-2 md:col-span-2">
              <div className="flex items-center space-x-2">
                <Checkbox
                  id="has_affordability_concerns"
                  checked={formData.has_affordability_concerns}
                  onCheckedChange={(checked) => handleCheckboxChange("has_affordability_concerns", checked as boolean)}
                />
                <Label htmlFor="has_affordability_concerns">Do you have affordability concerns?</Label>
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="city">
                City <span className="text-red-500">*</span>
              </Label>
              <Input
                id="city"
                name="city"
                value={formData.city}
                onChange={handleChange}
                required
                minLength={2}
                maxLength={15}
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="state">
                State <span className="text-red-500">*</span>
              </Label>
              <Input
                id="state"
                name="state"
                value={formData.state}
                onChange={handleChange}
                required
                minLength={2}
                maxLength={15}
              />
            </div>

            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="incident_description">
                Incident Description <span className="text-red-500">*</span>
              </Label>
              <Textarea
                id="incident_description"
                name="incident_description"
                value={formData.incident_description}
                onChange={handleChange}
                required
                minLength={10}
                maxLength={512}
                placeholder="Please describe what happened"
                className="min-h-[120px]"
              />
            </div>

            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="medical_costs">Medical Costs</Label>
              <Input
                id="medical_costs"
                name="medical_costs"
                value={formData.medical_costs}
                onChange={handleChange}
                placeholder="Approximate medical costs (if applicable)"
              />
            </div>
          </div>

          <div className="pt-4">
            <Button type="submit" className="w-full" disabled={isSubmitting}>
              {isSubmitting ? "Submitting..." : "Submit Case for Evaluation"}
            </Button>
          </div>
        </form>
      </CardContent>
    </Card>
  )
}
